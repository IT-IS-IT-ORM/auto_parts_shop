import _ from "lodash";

export function objectToUrlParams(object: object) {
  const params = _.map(
    object,
    (value, key) => `${encodeURIComponent(key)}=${encodeURIComponent(value)}`
  );

  return params.join("&");
}
