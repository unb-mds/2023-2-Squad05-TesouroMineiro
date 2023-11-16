import React, { useState } from 'react';
import Chart from 'react-apexcharts';

const Graficos = () => {
  const [selectedMunicipio, setSelectedMunicipio] = useState('NomeMunicipio1');
  const [selectedData, setSelectedData] = useState('30');

  const municipios = ['NomeMunicipio1', 'NomeMunicipio2', 'NomeMunicipio3', 'NomeMunicipio4', 'NomeMunicipio5', 'NomeMunicipio6', 'NomeMunicipio7', 'NomeMunicipio8', 'NomeMunicipio9'];
  const chartData = ['30', '40', '35', '50', '49', '60', '70', '91', '125'];

  const handleMunicipioChange = (e) => {
    setSelectedMunicipio(e.target.value);
  };

  const handleDataChange = (e) => {
    setSelectedData(e.target.value);
  };

  const dataExample = {
    options: {
      chart: {
        id: 'example',
      },
      xaxis: {
        categories: municipios,
      },
    },
    series: [
      {
        name: 'series-1',
        data: chartData,
      },
    ],
  };

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column', // Alteração aqui para organizar os elementos em coluna
        alignItems: 'center',
        height: '100vh',
      }}
    >
      <div style={{ marginBottom: '20px' }}>
        <label style={{ display: 'inline-block', marginBottom: '8px' }}>
          Escolha o município:
          <select value={selectedMunicipio} onChange={handleMunicipioChange}>
            {municipios.map((municipio) => (
              <option key={municipio} value={municipio}>
                {municipio}
              </option>
            ))}
          </select>
        </label>
        <br />
        <label>
          Dados:
          <select value={selectedData} onChange={handleDataChange}>
            {chartData.map((data) => (
              <option key={data} value={data}>
                {data}
              </option>
            ))}
          </select>
        </label>
      </div>
      <Chart options={dataExample.options} series={dataExample.series} type="bar" width={500} height={320} />
    </div>
  );
};

export default Graficos;
