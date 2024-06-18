import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function ShowDetailPage() {
  const { id } = useParams(); // Assume this is passed via the URL
  const [show, setShow] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`url/${id}`)
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Failed to fetch show details");
        }
        return resp.json();
      })
      .then((data) => setShow(data))
      .catch((error) => setError(error.message));
  }, [id]);

  if (error) {
    return <p>Error: {error}</p>;
  }

  if (!show) {
    return <p>Loading...</p>;
  }

  return (
    <div className="show-page">
      <div className="video">
        <iframe
          className="video"
          width="560"
          height="315"
          src={show.video}
          referrerPolicy="strict-origin-when-cross-origin"
          allowFullScreen
          title={show.name}
        />
      </div>
      <div className="text">
        <h3 className="name">{show.name}</h3>
        <h4 className="be">Summary:</h4>
        <p className="about">{show.summary}</p>
        <p className="category">Category: {show.category}</p>
        <p className="sub-category">Sub-category: {show.subCategory}</p>
        <p className="episode">Episode: {show.episode}</p>
        <p className="episode-summary">Episode Summary: {show.episodeSummary}</p>
      </div>
    </div>
  );
}

export default ShowDetailPage;
