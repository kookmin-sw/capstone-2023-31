import { combineReducers } from "redux";
import wishReducer from "./wishReducer";
import {persistReducer} from 'redux-persist';
import storage from 'redux-persist/lib/storage';
import { configureStore } from '@reduxjs/toolkit';
import { stringify } from "rc-field-form/es/useWatch";
import { joinPaths } from "@remix-run/router";

const persistConfig = {
  key: 'root',
  storage: storage,
  // whitelist: ["wishReducer"],
  // serialize: data => stringify(data),
  // deserailize: data => JSON.parse(data),
}

const reducer = combineReducers({wishReducer});
// console.log(reducer)
// const persistedReducer = persistReducer(persistConfig, reducer);
// const store = configureStore({
//   reducer: persistedReducer,
// })
// export default persistedReducer;
export default reducer;
// export default store;