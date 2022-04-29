import classes from './CardForm.module.css'

// WRAP component
function CardForm(props) {
    return(
        <div className={classes.cardForm}>
            {props.children}
        </div>
    );
}

export default CardForm;