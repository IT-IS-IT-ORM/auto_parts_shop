import _ from "lodash";

/**
 * @param {object} object
 * @param {'camel' | 'snake'} case_
 * @returns { object }
 */
export function convertKeysCase(
  object: object,
  case_: "camel" | "snake"
): object {
  if (Array.isArray(object)) {
    return object.map((item: object) => convertKeysCase(item, case_));
  }

  const newObj = {};

  _.forEach(object, (value, key) => {
    if (_.isObject(value)) {
      // @ts-ignore
      newObj[_[`${case_}Case`](key)] = convertKeysCase(value, case_);
    } else {
      // @ts-ignore
      newObj[_[`${case_}Case`](key)] = value;
    }
  });

  return newObj;
}
