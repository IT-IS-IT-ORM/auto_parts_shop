// 角色
export type allowedRole = "-1" | "0" | "1";

// 角色对象
export const role: {
  guest: "-1";
  provider: "0";
  consumer: "1";

  // 所有角色
  all: () => ["-1", "0", "1"];

  // 除 `roles` 以外的 所有角色
  exclude: (roles: allowedRole | allowedRole[]) => allowedRole[];
} = {
  guest: "-1",
  provider: "0",
  consumer: "1",

  // 所有角色
  all() {
    return ["-1", "0", "1"];
  },

  // 除 `roles` 以外的 所有角色
  exclude(roles) {
    let allRole: allowedRole[] = ["-1", "0", "1"];

    if (Array.isArray(roles)) {
      for (let role of roles) {
        allRole = allRole.filter((r) => r !== role);
      }

      return allRole;
    }

    return allRole.filter((role) => role !== roles);
  },
};
