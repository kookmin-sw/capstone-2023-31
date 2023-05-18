import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { Provider } from 'react-redux';
import  rootReducer from "./_reducer"
import { createStore } from 'redux';
import { persistStore } from 'redux-persist';
import { PersistGate } from 'redux-persist/integration/react';

const store = createStore(rootReducer);
const root = ReactDOM.createRoot(document.getElementById('root'));

const persistor = persistStore(store);

root.render(

  <Provider store={store}>
    <PersistGate persistor={persistor}>
      <App />
    </PersistGate>
  </Provider>

);