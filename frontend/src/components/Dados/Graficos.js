import React, { useState, useRef, useEffect } from 'react';
import Chart from 'react-apexcharts';

const Graficos = () => {
  const [selectedMunicipio, setSelectedMunicipio] = useState('NomeMunicipio1');
  const [selectedData, setSelectedData] = useState('30');
  const chartRef = useRef(null);

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
      className=''
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        height: '100%',
      }}
    >
      <div className='d-flex my-3 flex-column' style={{ marginBottom: '20px', width: '350px' }}>
        <div className='d-flex mb-2' style={{height:'70px'}}>
          <label className='input-group-text' >
            Município:
          </label>
          <select className='form-select' value={selectedMunicipio} onChange={handleMunicipioChange}>
            {municipios.map((municipio) => (
              <option key={municipio} value={municipio}>
                {municipio}
              </option>
            ))}
          </select>
        </div>
        <div className='d-flex' style={{height:'70px'}}>
          <label className='input-group-text'>
            Categoria:
          </label>
          <select className='form-select' value={selectedData} onChange={handleDataChange}>
            {chartData.map((data) => (
              <option key={data} value={data}>
                {data}
              </option>
            ))}
          </select>
        </div>
      </div>
      <div className='mt-5' style={{ maxWidth: '100%', maxHeight: '200px' }}>
        <Chart
          options={dataExample.options}
          series={dataExample.series}
          type="bar"
          width="450"
          height="400"
          ref={chartRef}
        />
      </div>
    </div>
  );
};

export default Graficos;
