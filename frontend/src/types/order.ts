import type { I_User } from "~/types/user";
import type { I_Product } from "~/types/product";

export interface I_Order {
  id: number;
  price: number;
  product: I_Product;
  buyer: I_User;
  createTime: string;
}
