// Types
import type { I_Response } from "~/types/api";
import type { I_Product } from "~/types/product";

// Utils
import _fetch from "~/service/fetch";

export const API_GetProductList = (): Promise<I_Response<I_Product[]>> =>
  _fetch.get("/product/");

export const API_GetFavoriteProductList = (): Promise<
  I_Response<I_Product[]>
> => _fetch.get(`/favorite/`);

export const API_GetProduct = (
  productId: number
): Promise<I_Response<I_Product>> => _fetch.get(`/product/${productId}/`);

export const API_UpdateProduct = (
  productId: number,
  data: Partial<I_Product>
): Promise<I_Response<I_Product>> =>
  _fetch.patch(`/product/${productId}/`, data);

export const API_AddProduct = (data: {}): Promise<I_Response<I_Product>> =>
  _fetch.post("/product/", data);

export interface API_SetFavorite_Data {
  productId: number;
  isFavorite: boolean;
}

export const API_SetFavorite = (
  data: API_SetFavorite_Data
): Promise<I_Response<null>> =>
  data.isFavorite
    ? _fetch.post("/favorite/", { product: data.productId })
    : _fetch.delete("/favorite/", { product: data.productId });
