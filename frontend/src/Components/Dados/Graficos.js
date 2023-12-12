import React, { useState, useRef, useEffect } from 'react';
import Chart from 'react-apexcharts';
import credsup from '../../Analises/CredSup.json';

const Graficos = () => {
  const [selectedMunicipio, setSelectedMunicipio] = useState();
  const [selectedData, setSelectedData] = useState('30');
  const [reportType, setReportType] = useState('geral');

  const [years, setYears] = useState([])
  const [selectedYear, setSelectedYear] = useState("2023")
  const chartRef = useRef(null);

  const [municipios, setMunicipios] = useState([]);
  const [chartData, setChartData] = useState([]);
  const [series, setSeries] = useState([]);
  const mesesDoAno = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
  ];

  // Mapeando os meses para seus índices
  const mesIndex = (month) => mesesDoAno.indexOf(month);

  useEffect(() => {
    let newarr = [];
    credsup.sort((a, b) => a.Municipio.localeCompare(b.Municipio));
    credsup.forEach((d) => {
      newarr.push(d.Municipio);
    });
    setMunicipios([...newarr]);
    setSelectedMunicipio(newarr[0])

    fetchChartData(newarr[0], selectedMunicipio, 'geral', '2023')
    let years = []
    credsup.forEach((d) => {
      if (newarr[0] == d.Municipio) {
        d.Analises.forEach((a) => {
          years.push(a.Ano)
        })
      }
    })
    setYears([...years])

  }, []);

  const handleMunicipioChange = (e) => {
    setSelectedMunicipio(e.target.value);

    let newarr = []
    credsup.forEach((d) => {
      if (e.target.value == d.Municipio) {
        d.Analises.forEach((a) => {
          newarr.push(a.Ano)
        })
      }
    })

    newarr.sort(function (a, b) {
      return b - a;
    });

    setYears([...newarr])
    fetchChartData(e.target.value, selectedData, reportType);
  };

  const handleDataChange = (e) => {
    setSelectedData(e.target.value);
    fetchChartData(selectedMunicipio, e.target.value, reportType);
  };

  const handleReportTypeChange = (e) => {
    setReportType(e.target.value);
    fetchChartData(selectedMunicipio, selectedData, e.target.value);
  };

  const handleYearChange = (e) => {
    setSelectedYear(e.target.value)
    fetchChartData(selectedMunicipio, selectedData, reportType, e.target.value);
  }

  const fetchChartData = (selectedMunicipio, selectedData, reportType, year = '2023') => {
    let series = [];
    let data = [];
    credsup.forEach((d) => {
      if (d.Municipio === selectedMunicipio) {
        d.Analises.forEach((a) => {
          if ((reportType === 'geral')) {
            series.push(a.SomaAnual);
            data.push(a.Ano);
          } else if (a.Ano == year) {
            data = Object.keys(a.Meses)
            series = Object.values(a.Meses)
            data.sort((a, b) => mesIndex(a) - mesIndex(b));
            series.sort((a, b) => mesIndex(a) - mesIndex(b));
          }
        });
      }
    });

    setChartData([...data]);
    setSeries([...series]);
  };

  const dataExample = {
    options: {
      chart: {
        id: 'example',
      },
      xaxis: {
        categories: chartData,
      },
      yaxis: {
        labels: {
          formatter: function (numero) {
            const numeroFormatado = 'R$ ' + numero.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, ".");
            return numeroFormatado;
          }
        }
      },
      dataLabels: {
        enabled: false,
        formatter: function (val) {
          const numeroFormatado = 'R$ ' + val.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, ".");
          return numeroFormatado;
        },
      },
    },
    series: [
      {
        name: '',
        data: series,
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
      }}
    >
      <div className='d-flex flex-column my-3 w-75 justify-content-center' style={{ marginBottom: '20px', width: '350px' }}>
        <div className='d-flex mb-2' style={{ height: '70px' }}>
          <label className='input-group-text'>
            Município:
          </label>
          <select className='form-select' value={selectedMunicipio} onChange={(e) => handleMunicipioChange(e)}>
            {municipios.map((municipio) => (
              <option key={municipio} value={municipio}>
                {municipio}
              </option>
            ))}
          </select>
        </div>
        <div className='d-flex mb-2' style={{ height: '70px' }}>
          <label className='input-group-text'>
            Categoria:
          </label>
          <select className='form-select' value={selectedData} onChange={handleDataChange}>
            <option value>
              Crédito Suplementar
            </option>
          </select>
        </div>
        <div className='d-flex mb-2' style={{ height: '70px' }}>
          <label className='input-group-text'>
            Tipo de Relatório:
          </label>
          <select className='form-select' value={reportType} onChange={handleReportTypeChange}>
            <option value='geral'>Geral</option>
            <option value='anual'>Anual</option>
          </select>
          {reportType == 'anual' && (
            <select className='form-select' value={selectedYear} onChange={(e) => handleYearChange(e)}>
              {years.map((y, id) => (
                <option key={id} value={y}>
                  {y}
                </option>
              ))}
            </select>
          )}
        </div>
      </div>
      <div className='mt-5 mb-5 grafico'>
        <Chart
          options={dataExample.options}
          series={dataExample.series}
          type="bar"
          ref={chartRef}
        />
      </div>
    </div>
  );
};

export default Graficos;
