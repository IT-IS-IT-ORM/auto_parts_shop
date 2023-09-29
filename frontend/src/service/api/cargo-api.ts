// Types
import type { I_Response } from "~/types/api";
import type { I_Cargo } from "~/types/cargo";

// Utils
import _fetch from "~/service/fetch";

export const API_GetCargoList = (): Promise<I_Response<I_Cargo[]>> =>
  _fetch.get("/cargo/");

export const API_AddCargo = (data: {
  code: string;
  name: string;
}): Promise<I_Response<I_Cargo>> => _fetch.post("/cargo/", data);
