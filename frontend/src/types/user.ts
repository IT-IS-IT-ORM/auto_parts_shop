import type { allowedRole } from "~/utils/role";

export interface I_User {
  id: number;
  role: allowedRole;
  fullname: string;
  phone: string;
  createTime: string;
  token: string;
}
