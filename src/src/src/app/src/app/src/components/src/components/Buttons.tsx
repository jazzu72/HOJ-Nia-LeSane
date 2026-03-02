import React from "react";

type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  label: string;
};

const Button: React.FC<ButtonProps> = ({ label, ...rest }) => {
  return <button {...rest}>{label}</button>;
};

export default Button;
