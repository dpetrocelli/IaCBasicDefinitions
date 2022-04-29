import { Link } from 'react-router-dom';

import classes from './mainNavigation.module.css';
import { useContext } from 'react';

function MainNavigation() {
    // NEED REDUX HERE

    return(
        <header className={classes.header}>
            <div className={classes.logo}>Club Geminis</div>
            <nav>
                <ul>
                    <li>
                        <Link to='/actividades'>Actividades</Link>
                    </li>
                    <li>
                        <Link to='/planes'>Planes</Link>
                    </li>
                    <li>
                        <Link to='/contactos'>Contactos</Link>
                    </li>

                    {/* {authCtx.isLogged ? <LoggedSection userName={''} /> : <NotLoggedSection />}                 */}
                    <NotLoggedSection />
                </ul>
            </nav>
        </header>
    );
}

function LoggedSection(props) {
    // TODO cmopletar para que muestre el nombre y la imagen del usuario
    return (
        <li>
            <Link to='/login'>{props.userName}</Link>
        </li> 
    );
}

function NotLoggedSection() {
    
    return (
        <li>
            <Link to='/login'>Iniciar sesion/Registrarse</Link>
        </li> 
    );
}

export default MainNavigation;