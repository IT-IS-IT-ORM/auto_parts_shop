const HOST = "http://127.0.0.1";
const PORT = "8000";

const BASE_URL = `${HOST}:${PORT}/api`;

// Types
import type { I_Response, I_DefaultHeaders, HttpMethod } from "~/types/api";
// Store
import { defaultUserState } from "~/stores/user";
// Utils
import _ from "lodash";

interface I_FetchOptions {
  headersCustomize?: (defaultHeaders: I_DefaultHeaders) => HeadersInit;
  payloadCustomize?: () => BodyInit | null | undefined;
}

function requestWithData(method: Exclude<HttpMethod, "GET">) {
  return async <T>(
    url: string,
    data?: object,
    options?: I_FetchOptions
  ): Promise<I_Response<T>> => {
    // API endpoint
    url = `${BASE_URL}${url}`;
    // 用户 Token
    const { token } = localStorage.get("user", defaultUserState);

    // 如果有 data
    if (data) {
      // 如果要 自定义上传数据
      if (options?.payloadCustomize) {
        // @ts-ignore ( 一般返回 FormData )
        data = options.payloadCustomize();
      } else {
        // @ts-ignore 默认 data 是 object 类型, 转为 snake case
        data = JSON.stringify(convertKeysCase(data, "snake"));
      }
    }

    let defaultHeaders = {
      Authorization: token,
      Accept: "application/json",
      "Content-Type": "application/json",
    };

    // if data is FormData, then "Content-Type" is automatically set by browser
    if (data instanceof FormData) {
      defaultHeaders = _.omit(
        defaultHeaders,
        "Content-Type"
      ) as I_DefaultHeaders;
    }

    // 自定义 请求头
    const headers =
      (options?.headersCustomize?.(defaultHeaders) as I_DefaultHeaders) ??
      defaultHeaders;

    const response = await fetch(url, {
      method,
      headers,
      body: data as any as string | FormData,
    }).catch(() => {
      return { isSuccess: false, message: "apiError.500" };
    });

    if (response instanceof Response) {
      data = await response.json();

      if (response.status >= 200 && response.status < 300) {
        return convertKeysCase(data!, "camel") as any as I_Response<T>;
      }

      return await Promise.reject(data);
    }

    return await Promise.reject(response);
  };
}

export default {
  async get<T>(url: string, params?: object): Promise<I_Response<T>> {
    // 在 url 上拼接 params
    if (params) {
      url += `?${objectToUrlParams(params)}`;
    }
    url = `${BASE_URL}${url}`;
    // 用户 Token
    const { token } = localStorage.get("user", defaultUserState);

    let defaultHeaders = {
      Authorization: token,
      Accept: "application/json",
      "Content-Type": "application/json",
    };

    const response = await fetch(url, {
      method: "GET",
      headers: defaultHeaders,
    }).catch(() => {
      return { isSuccess: false, message: "apiError.500" };
    });

    if (response instanceof Response) {
      const data = await response.json();

      if (response.status >= 200 && response.status < 300) {
        return convertKeysCase(data!, "camel") as any as I_Response<T>;
      }

      return await Promise.reject(data);
    }

    return await Promise.reject(response);
  },

  post: requestWithData("POST"),
  patch: requestWithData("PATCH"),
  put: requestWithData("PUT"),
  delete: requestWithData("DELETE"),
};
