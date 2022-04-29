import { useEffect } from "react";
import CardUserList from "../components/ui/CardUserList";
import userService from "../services/user.service";

const users = [
    {
        dni: 12345678,
        firstName: 'seba',
        lastName: 'marchetti',
        age: 23,
        mail: 'fakemail@mail.com',
        phone: '2323-123456',
        roles: [
            'Admin',
            'Profesor'
        ]
    },
    {
        dni: 12345678,
        firstName: 'angel',
        lastName: 'Luis',
        age: 23,
        mail: 'fakemail@mail.com',
        phone: '2323-123456',
        roles: [
            'Admin',
            'Profesor'
        ]
    }
]



function UserListPage() {

    const isAdmin = false;
    const userList = users;

    // useEffect( () => {
    //     // Gets all users. If 403 forbidden, show "not allowed" sign
    //     userService.getUserList()
    //         .then()
    //         .catch((error) => {

    //         });
    // }, []);

    return (
        <section>
            <h1>Lista de Usuarios</h1>
            {/* <CardUserList users={userList}/> */}
            <section>
                <ul>
                {userList.map((user) => {
                    return <CardUserList user={user}/>;
                })}
                </ul>
            </section>
        </section>
    );
}

export default UserListPage;