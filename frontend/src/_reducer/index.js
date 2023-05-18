import { combineReducers } from "redux";
import wishReducer from "./wishReducer";
import { persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';

const persistConfig = {
  key: 'root',
  storage: storage,
}

const reducer = combineReducers({wishReducer});
const persistedReducer = persistReducer(persistConfig, reducer);

export default persistedReducer;