import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
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

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
