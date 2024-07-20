import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import api from '../../services/api';

function LineageGraph() {
  const svgRef = useRef();

  useEffect(() => {
    const fetchLineageData = async () => {
      try {
        const response = await api.get('/lineage');
        const data = response.data;
        createGraph(data);
      } catch (error) {
        console.error('Failed to fetch lineage data:', error);
      }
    };
    fetchLineageData();
  }, []);

  const createGraph = (data) => {
    const svg = d3.select(svgRef.current);
    const width = 800;
    const height = 600;

    const simulation = d3.forceSimulation(data.nodes)
      .force("link", d3.forceLink(data.links).id(d => d.id))
      .force("charge", d3.forceManyBody())
      .force("center", d3.forceCenter(width / 2, height / 2));

    const link = svg.append("g")
      .selectAll("line")
      .data(data.links)
      .join("line")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6);

    const node = svg.append("g")
      .selectAll("circle")
      .data(data.nodes)
      .join("circle")
      .attr("r", 5)
      .attr("fill", d => d.group === 1 ? "#ff0000" : "#00ff00");

    node.append("title")
      .text(d => d.id);

    simulation.on("tick", () => {
      link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

      node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);
    });
  };

  return <svg ref={svgRef} width={800} height={600}></svg>;
}

export default LineageGraph;