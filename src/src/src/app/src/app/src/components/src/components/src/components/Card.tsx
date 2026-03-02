import React from "react";

type CardProps = {
  title: string;
  children?: React.ReactNode;
};

const Card: React.FC<CardProps> = ({ title, children }) => {
  return (
    <section style={{ border: "1px solid #444", padding: "1rem", borderRadius: 8 }}>
      <h2>{title}</h2>
      {children}
    </section>
  );
};

export default Card;
