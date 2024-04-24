// Types
import type { I_Response } from "~/types/api";
import type { I_Order } from "~/types/order";

// Utils
import _fetch from "~/service/fetch";

export const API_CreateOrder = (
  productId: number
): Promise<I_Response<I_Order>> => _fetch.post("/order/", { productId });

export const API_GetOrderList = (): Promise<I_Response<I_Order[]>> =>
  _fetch.get("/order/");
