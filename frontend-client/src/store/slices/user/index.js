import { createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const initialState = {
    username: '',
}

export const userSlice = createSlice({
    name: 'userData',
    initialState,
    reducers: {
        setUserData: (state, action) => {
            state.username = action.payload
        },
        getUsername: (state, action) => {
            return initialState.username;
        }
    }
})

export const {setUserData, getUsername} = userSlice.actions;

export default userSlice.reducer



export const fetchUserData = () => {
    return (dispatch) => {
        //TODO preparar para obtener los datos de los usuarios
        // axios.get()
        //     .then((response) => {
        //         dispatch(setUserData(response));
        //     })
        //     .catch((error) => {

        //     })
        // dispatch(setUserData('user'));

    }
}