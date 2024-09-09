import React, { useState, useEffect, useRef } from "react";
import DestList from "./DestList";
import Card from "../UI/Card/Card";
import classes from "./Home.module.css";

const Home = (props) => {
  const [destList, setDestList] = useState([]);
  const [destSearchWord, setDestSearchWord] = useState("Denmark");
  const searchWordref = useRef();

  const fetchSearchData = async (enteredWord) => {
    const urlPath = "http://127.0.0.1:8000/get-data";
    const headers = new Headers();
    headers.set("Content-Type", "application/json");
    try {
      const jsonCreds = {
        name: enteredWord,
      };
      const response = await fetch(urlPath, {
        method: "POST",
        headers: headers,
        body: JSON.stringify(jsonCreds),
      });

      if (response.ok) {
        const data = await response.json();
        setDestList(data);
      }
    } catch (error) {
      console.log("Error fetching data from Backend:", error);
    }
  };

  useEffect(() => {
    fetchSearchData(destSearchWord);
  }, [destSearchWord]);

  if(destList.length !== 0){
    console.log(destList.message[0].dest_desc)
  }
  
  const destListMapped = destList.length !== 0 ?
        <DestList
          name={destList.message[0].dest_name}
          desc={destList.message[0].dest_desc}
        /> : "";

  const songSearchHandler = () => {
    setDestSearchWord(searchWordref.current.value);
  };

  return (
    <React.Fragment>
      <Card className={classes.home}>
        <div>
          <input placeholder="Enter a Destination name" ref={searchWordref} />
          <button onClick={songSearchHandler}>Search</button>
        </div>
        <h1>List of Top Places from Api</h1>
        <ul>{destListMapped}</ul>
      </Card>
    </React.Fragment>
  );
};

export default Home;
