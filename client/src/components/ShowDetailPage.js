import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./ShowsDetail.css";

function ShowDetailPage() {
  const { id } = useParams();
  const [show, setShow] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentEpisode, setCurrentEpisode] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:5555/show/${id}`)
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Failed to fetch show details");
        }
        return resp.json();
      })
      .then((data) => {
        setShow(data);
        if (data.episodes && data.episodes.length > 0) {
          setCurrentEpisode(data.episodes[0]); // Set the first episode as the default
        }
        setLoading(false);
      })
      .catch((error) => {
        setError(error.message);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  const handleEpisodeClick = (episode) => {
    setCurrentEpisode(episode);
  };

  return (
    <div className="show-page">
      {currentEpisode && (
         <div className="video-container">
         <iframe
           className="video"
           src={currentEpisode.video}
           referrerPolicy="strict-origin-when-cross-origin"
           allowFullScreen
           title={currentEpisode.title}
         />
        </div>
      )}
      <div className="episodes-section">
        <h2 className="section-title">Episodes</h2>
        <div className="episodes-grid">
          {show.episodes && show.episodes.length > 0 ? (
            show.episodes.map((episode) => (
              <div
                key={episode.id}
                className="episode-card"
                onClick={() => handleEpisodeClick(episode)}
              >
                <img
                  className="episode-thumbnail"
                  src={show.image}
                  alt={episode.title}
                />
                <div className="episode-info">
                  <h3 className="episode-title">{episode.title}</h3>
                  <p className="episode-summary">{episode.summary}</p>
                </div>
              </div>
            ))
          ) : (
            <p>No episodes available.</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default ShowDetailPage;
