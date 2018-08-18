const webpack = require('webpack');

module.exports = env => {
  // create a nice object from the env variable

  return {
    mode: 'development',
    entry: __dirname + '/js/index.jsx',
    output: {
      path: __dirname + '/dist',
      filename: 'bundle.js',
    },
    resolve: {
      extensions: ['.js', '.jsx', '.css', '*']
    },
    devServer: {
      publicPath: '/dist/',
      host: '0.0.0.0',
      port: 8080
    },
    module: {
      rules: [
        {
          test: /\.(jsx|js)?/,
          exclude: /node_modules/,
          use: ['babel-loader']
        },
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader']
        }
      ]
    },
    plugins: [
      new webpack.DefinePlugin({ 'process.env.API_HOST': JSON.stringify(env.API_HOST) })
    ],
    performance: {
      hints: false
    }
  }
};
