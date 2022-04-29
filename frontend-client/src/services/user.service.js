import axios from 'axios';
import authHeader from './auth-Header';

const API_URL = 'https://sip-api-dev.herokuapp.com/';

class UserService {

    /*

        TODO PONER AQUI TODOS LOS SERVICIOS A PEDIR DEL BACK

    */


    getUserList() {
        return axios.get(API_URL + 'all');
    }

    // getUserBoard() {
    //     return axios.get(API_URL + 'user', { headers: authHeader() });
    // }

    // getModeratorBoard() {
    //     return axios.get(API_URL + 'mod', { headers: authHeader() });
    // }

    // getAdminBoard() {
    //     return axios.get(API_URL + 'admin', { headers: authHeader() });
    // }

}

export default new UserService();