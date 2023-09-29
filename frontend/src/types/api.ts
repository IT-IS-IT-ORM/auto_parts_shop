export interface I_Response<T> {
  isOk: boolean;
  reLogin: boolean;
  data: T;
  message: string;
}

export type I_DefaultHeaders = HeadersInit & {
  Authorization: string;
  Accept: string;
  "Content-Type": string;
};

export type HttpMethod = "GET" | "POST" | "PATCH" | "PUT" | "DELETE";