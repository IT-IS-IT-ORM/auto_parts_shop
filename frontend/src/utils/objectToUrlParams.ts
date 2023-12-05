import _ from "lodash";

export function objectToUrlParams(object: object) {
  const params = _.map(object, (value, key) => {
    if (Array.isArray(value)) {
      if ((value as []).filter((item) => item !== null).length === 0) {
        return "";
      }
      return `${encodeURIComponent(key)}=${(value as []).join(",")}`;
    }

    return `${encodeURIComponent(key)}=${encodeURIComponent(value)}`;
  });

  return params.join("&");
}
