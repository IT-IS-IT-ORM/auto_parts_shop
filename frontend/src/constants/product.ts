// Types
import type { I_CategoryFilter, I_SubCategory } from "~/types/product";

export const INITIAL_PRODUCT_FORMSTATE = {
  title: "",
  description: "",
  price: 5000,
  isNew: true,
  type: "sm",
  category: null as I_SubCategory["id"] | null,
  applicable: [] as I_CategoryFilter["id"][],
  gallery: [] as File[],
};
