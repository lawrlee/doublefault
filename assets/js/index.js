import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import {ApolloClient, createNetworkInterface, ApolloProvider} from 'react-apollo'
import {BrowserRouter} from 'react-router-dom'
import * as Blueprint from "@blueprintjs/core";

const client = new ApolloClient({
  networkInterface: createNetworkInterface({uri: '/graphql'}),
});

ReactDOM.render(
  <BrowserRouter>
    <ApolloProvider client={client}>
      <App/>
    </ApolloProvider>
  </BrowserRouter>
  ,
  document.getElementById('root')
);
