// Types
import type { I_Response } from "~/types/api";
import type { I_Product } from "~/types/product";
// Vue
import { toRaw } from "vue";
// Utils
import _fetch from "~/service/fetch";

interface I_ProductQuery {
  type: I_Product["type"] | null;
  isNew: boolean;
  hasImage: boolean;
  minPrice: number | null;
  maxPrice: number | null;
  categories: number[];
  subCategories: number[];
}

export const API_GetProductList = (
  queryParams: Partial<I_ProductQuery>
): Promise<I_Response<I_Product[]>> => _fetch.get("/product/", queryParams);

export const API_GetFavoriteProductList = (): Promise<
  I_Response<I_Product[]>
> => _fetch.get(`/favorite/`);

export const API_GetMyProductList = () =>
  _fetch.get<I_Product[]>("/product/mine/");

export const API_GetProduct = (
  productId: number
): Promise<I_Response<I_Product>> => _fetch.get(`/product/${productId}/`);

export const API_UpdateProduct = (
  productId: number,
  data: Partial<I_Product>
): Promise<I_Response<I_Product>> =>
  _fetch.patch(`/product/${productId}/`, data);

export const API_AddProduct = (data: {}): Promise<I_Response<I_Product>> =>
  _fetch.post("/product/", data, {
    payloadCustomize() {
      const formData = new FormData();
      // @ts-ignore
      Object.entries(data).forEach(([key, value]) => {
        if (key === "applicable") {
          value = (value as number[]).join(",");
        } else if (key === "gallery") {
          (value as File[]).forEach((file) => {
            formData.append(key, file);
          });
          return;
        }
        // @ts-ignore
        formData.append(key, toRaw(value).toString());
      });

      return formData;
    },
  });

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

export const API_FetchCategories = (): Promise<
  I_Response<I_Product["category"]>
> => _fetch.get("/category/");
