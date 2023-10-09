// Types
import type { I_Response } from "~/types/api";
import type { I_Product } from "~/types/product";

// Utils
import _fetch from "~/service/fetch";

export const API_GetProductList = (): Promise<I_Response<I_Product[]>> =>
  _fetch.get("/product/");

export const API_AddProduct = (data: {}): Promise<I_Response<I_Product>> =>
  _fetch.post("/product/", data);
