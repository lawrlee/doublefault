const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const BundleClean = require('webpack-bundle-clean');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
  devtool: "eval-source-map",
  context: __dirname,
  entry: ['./assets/js/index', './assets/css/stylesheet.css'],
  output: {
    devtoolLineToLine: true,
    sourceMapFilename: "[name].js.map",
    path: path.resolve('./assets/bundles/'),
    pathinfo: true,
    filename: "[name]-[hash].js"
  },

  plugins: [
    new BundleClean({filename: './webpack-stats.json'}),
    new BundleTracker({filename: './webpack-stats.json', indent: '  '}),
    new ExtractTextPlugin("[name]-[hash].css"),
  ],

  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        }
      },
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: "css-loader"
        })
      },
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
          'file-loader'
        ]
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          'file-loader'
        ]
      }
    ],
  },

  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.jsx']
  },
}