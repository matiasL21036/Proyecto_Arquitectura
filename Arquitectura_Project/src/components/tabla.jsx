import { useEffect, useState } from 'react';

const CargoTable = () => {
  const [cargos, setCargos] = useState([]);
  const [newCargo, setNewCargo] = useState('');
  const [error, setError] = useState(null);

  // Obtener cargos de la API
  const fetchCargos = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/cargos');
      if (!response.ok) {
        throw new Error('Error al obtener cargos');
      }
      const result = await response.json();
      setCargos(result);
    } catch (error) {
      setError(error.message);
    }
  };

  useEffect(() => {
    fetchCargos();
  }, []);

  // Enviar nuevo cargo a la API
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null); // Resetear error al intentar agregar un nuevo cargo

    try {
      const response = await fetch('http://localhost:5000/api/cargos/crear', { // Cambia la ruta a '/crear' según tu API
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombrecargo: newCargo }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Error al agregar cargo');
      }

      setNewCargo('');
      fetchCargos(); // Vuelve a obtener los cargos después de agregar uno nuevo
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      {error && <p>Error: {error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={newCargo}
          onChange={(e) => setNewCargo(e.target.value)}
          placeholder="Agregar nuevo cargo"
          required
        />
        <button type="submit">Agregar</button>
      </form>
      <table>
        <thead>
          <tr>
            <th>ID Cargo</th>
            <th>Nombre Cargo</th>
          </tr>
        </thead>
        <tbody>
          {cargos.map((cargo) => (
            <tr key={cargo.idcargo}>
              <td>{cargo.idcargo}</td>
              <td>{cargo.nombrecargo}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CargoTable;
