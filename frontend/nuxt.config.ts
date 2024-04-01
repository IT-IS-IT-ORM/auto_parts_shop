// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  srcDir: "src/",

  ssr: false,

  devtools: { enabled: false },

  css: [
    "~/assets/style/variables.css",
    "~/assets/style/reset.css",
    "~/assets/style/antd.css",
    // Global class
    "~/assets/style/itisit-container.css",
    "~/assets/style/itisit-icon.css",
  ],

  modules: ["nuxt-icon", "@pinia/nuxt", "nuxt-lodash"],

  nitro: {
    prerender: {
      failOnError: false,
    },
  },

  app: {
    pageTransition: { name: "page", mode: "out-in" },
  },
});
