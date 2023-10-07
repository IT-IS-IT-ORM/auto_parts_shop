function dynamicAsset(path: string): string {
  // @ts-ignore
  const assets = import.meta.glob("~/assets/**/*", {
    eager: true,
    import: "default",
  });

  return assets[`/assets/${path}`];
}

dynamicAsset.image = function (filename: string): string {
  return dynamicAsset(`image/${filename}`);
};

dynamicAsset.icon = function (filename: string): string {
  return dynamicAsset(`icon/${filename}`);
};

export default dynamicAsset;
