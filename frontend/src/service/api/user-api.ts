// Types
import type { I_Response } from "~/types/api";
import type { I_User } from "~/types/user";

// Utils
import _fetch from "~/service/fetch";

export const API_Login = (data: {
  phone: string;
  password: string;
}): Promise<I_Response<I_User>> => _fetch.post("/auth/login/", data);

export const API_Register = (data: {
  phone: string;
  fullname: string;
  password: string;
}): Promise<I_Response<I_User>> => _fetch.post("/auth/register/", data);

export const API_UpdateInfo = (
  userId: number,
  data: {
    phone?: string;
    fullname?: string;
  }
): Promise<I_Response<I_User>> => _fetch.patch(`/user/${userId}/`, data);

export const API_ChangePassword = (data: {
  password: string;
  newPassword: string;
}): Promise<I_Response<I_User>> => _fetch.post(`/auth/change-password/`, data);
