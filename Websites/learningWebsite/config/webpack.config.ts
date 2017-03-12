import * as path from 'path';
import * as webpack from 'webpack';
const ExtractTextPlugin = require("extract-text-webpack-plugin");
var WebpackNotifierPlugin = require('webpack-notifier');

const rootPath = path.resolve(__dirname, "../");
const assetPath = path.resolve(rootPath, "./Assets/scripts");



const config: webpack.Configuration = {
    watch: true,
    
    context: path.resolve(__dirname, ".."),
    entry: "./App/index.tsx",
    output: {
        path: assetPath,
        publicPath: "scripts",
        filename: "main.js"
    },
    devtool: "source-map",
    resolve: {
        extensions: [".ts", ".tsx", ".js", ".jsx"],
    },
    module: {
        loaders: [
            {
                test: /\.tsx?$/,
                loader: "ts-loader"
            },
            { 
                test: /\.js(x?)$/,
                loader: 'babel-loader', 
                exclude: "/node_modules/",
                query: {
                    presets: ["react", "es2015"]
                }
            }
        ]
    },
    plugins: [
        new webpack.DefinePlugin({ 'process.env': { 'NODE_ENV':
'"development"' } }),
        new ExtractTextPlugin('../styles/[name].css'),
        new WebpackNotifierPlugin({ alwaysNotify: true })
    ]
};

export default config;