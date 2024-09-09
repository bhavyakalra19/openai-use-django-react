import classes from './songList.module.css';

const DestList = (props) => {
  return (
    <li className={classes.song}>
      <div>
        <h3 className={classes.name}>{props.name}</h3>
        <h3 className={classes.name}>{props.desc}</h3>
      </div>
    </li>
  );
};

export default DestList;
