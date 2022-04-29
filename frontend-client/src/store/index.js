import { configureStore } from "@reduxjs/toolkit";
import userDataReducers from './slices/user'

export default configureStore({
    reducer: {
        userData: userDataReducers
    }
})

