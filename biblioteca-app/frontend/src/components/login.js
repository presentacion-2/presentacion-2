import React, { useState } from "react";

async function loginUser(credentials) {
  const response = await fetch("http://127.0.0.1:5000/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });
  
  if (response.ok) {
    const data = await response.json();
    return data;
  } else {
    throw new Error("Usuario o contraseña incorrectos");
  }
}

export default function Login({ setToken }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(""); // Nuevo estado para el mensaje de error

  const handleSubmit = async (e) => {
    e.preventDefault();
    let payload = {
      email: username,
      password: password,
    };
    
    try {
      const response = await loginUser(payload);
      setToken(response.token);
      localStorage.setItem("IdUsuario", JSON.stringify(response.id_usuario));
      localStorage.setItem("NombreUsuario", response.email);
      localStorage.setItem("TipoUsuario", response.tipo);
      window.location.reload();
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div class="card text-center">
      <div class="card-header">
        <center>
          <h3 style={{ fontWeight: 1000 }}>
            Bienvenido al portal de la biblioteca de la universidad de Salamanca
          </h3>
        </center>
      </div>
      <div class="card-body">
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label for="inputUsernameLogin" class="form-label">
              Email
            </label>
            <input
              type="username"
              class="form-control"
              id="inputUsernameLogin"
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>

          <div class="mb-3">
            <label for="inputPasswordLogin" class="form-label">
              Contraseña
            </label>
            <input
              type="password"
              class="form-control"
              id="inputPasswordLogin"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          {error && <p style={{ color: "red" }}>{error}</p>} {/* Mostrar el mensaje de error si existe */}
          <button type="submit" className="btn btn-primary">
            Ingresar
          </button>
        </form>
      </div>
    </div>
  );
}
