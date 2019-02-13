module.exports = {

    rootDir : '../',
    setupFilesAfterEnv : ["<rootDir>/client/node_modules/enzyme", "<rootDir>/client/node_modules/enzyme-adapter-react-16", "<rootDir>/client/node_modules/enzyme-adapter-utils"],
    testEnvironment: "node",
    testMatch: [
    "**/**/*.test.ts?(x)", "**/**/*.test.js?(x)", "**/?(*.)+(spec|test).js?(x)"
    ],
    modulePaths: [
    "<rootDir>/client/node_modules"
    ],
    globals: {
    "NODE_ENV": "test"
    },
    verbose: true,
    moduleFileExtensions: [
    "ts",
    "tsx",
    "js",
    "jsx",
    "json"
    ],
    // transform: {
    // "^.+\\.tsx?$": "<rootDir>/node_modules/ts-jest/preprocessor.js"
    // },
    transformIgnorePatterns: ["client/node_modules/react/"], // <-- this allows babel to load only the node modules I need (which is lodash-es) and ignore the rest
    // some coverage and results processing options
    collectCoverage: true,
    collectCoverageFrom: [
    "src/components/**/*.ts?(x)",
    "src/components/**/*.js?(x)",
    "src/reducers/**/*.ts?(x)",
    "src/reducers/**/*.js?(x)"
    ],
    coverageDirectory: "./coverage",
    coverageReporters: ["json", "lcov", "text"]
    };