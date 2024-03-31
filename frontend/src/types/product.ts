import type { I_User } from "~/types/user";

export interface I_Category {
  id: number;
  title: string;
  parent: null;
}
export interface I_SubCategory {
  id: number;
  title: string;
  parent: number;
}

export interface I_ProductImage {
  id: number;
  image: string;
}

export interface I_Product {
  id: number;
  title: string;
  description: string;
  price: number;
  isNew: boolean;
  isFavorite: boolean;
  views: number;
  gallery: I_ProductImage[];
  type: "sm" | "md" | "lg";
  createTime: string;
  seller: Omit<I_User, "token">;
  category: Array<I_Category | I_SubCategory>;
  applicable: I_SubCategory[];
}

export interface I_CategoryFilter extends I_Category {
  isSelected: boolean;
  isCollapsed: boolean;
  subCategories: I_CategoryFilter[];
}
