module.exports = {
  arrowParens: "always",
  semi: true,
  trailingComma: "all",
  singleQuote: true,
  objectWrap: "collapse",
  bracketSpacing: true,
  bracketSameLine: false,
  tabWidth: 2,
  printWidth: 80,
  useTabs: false,
  // pnpm doesn't support plugin autoloading
  // https://github.com/tailwindlabs/prettier-plugin-tailwindcss#installation
  plugins: ["prettier-plugin-tailwindcss"],
};
