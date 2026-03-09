<script lang="ts">
  import { onMount } from 'svelte';
  import { scale } from 'svelte/transition';

  // Mock Qiskit results – in real version call FastAPI /api/quantum/branch
  let probabilities = [0.42, 0.33, 0.25]; // sum ≈ 1
  let selectedBranch: number | null = null;
  let isMeasuring = false;

  const branches = [
    { name: 'AGGRESSIVE_STRIKE', color: '#ff4444', strategy: 'Al Davis', objective: 'Max vertical gain' },
    { name: 'STRATEGIC_EFFICIENCY', color: '#44ff44', strategy: 'Sun Tzu', objective: 'Subdue without fighting' },
    { name: 'TECHNICAL_FEASIBILITY', color: '#4488ff', strategy: 'Kano', objective: 'Build integrity first' }
  ];

  async function measure() {
    isMeasuring = true;
    selectedBranch = null;

    // Simulate Qiskit measurement delay
    await new Promise(r => setTimeout(r, 1800));

    // Weighted random selection
    let r = Math.random();
    let cumulative = 0;
    for (let i = 0; i < probabilities.length; i++) {
      cumulative += probabilities[i];
      if (r <= cumulative) {
        selectedBranch = i;
        break;
      }
    }

    isMeasuring = false;
  }

  onMount(() => {
    // Optional: auto-measure on mount for demo
    // measure();
  });
</script>

<div class="quantum-container">
  <h2 class="quantum-title">Quantum Branching Visualizer</h2>
  <p class="quantum-subtitle">Superposition → Measurement Collapse</p>

  <div class="circuit-wrapper">
    <!-- Quantum circuit visualization -->
    <div class="qubit-lines">
      {#each [0,1,2] as q}
        <div class="qubit-line" transition:scale={{ duration: 600, delay: q * 150 }}>
          Q{q}
        </div>
      {/each}
    </div>

    <div class="gates">
      <div class="gate hadamard" transition:scale>H</div>
      <div class="gate cx" transition:scale>CX</div>
      <div class="gate measure" transition:scale>M</div>
    </div>
  </div>

  <div class="branches">
    {#each branches as branch, i}
      <div
        class="branch-card"
        class:selected={selectedBranch === i}
        class:measuring={isMeasuring}
        on:click={measure}
        transition:scale={{ duration: 400 }}
      >
        <div class="branch-header" style:background={branch.color}>
          {branch.name}
        </div>
        <div class="branch-body">
          <strong>{branch.strategy}</strong>
          <p>{branch.objective}</p>
          {#if selectedBranch === i}
            <div class="collapse-result">
              COLLAPSED → Chosen
            </div>
          {/if}
        </div>
        <div class="probability-bar">
          <div class="bar-fill" style:width={`${probabilities[i] * 100}%`}></div>
        </div>
      </div>
    {/each}
  </div>

  <button class="measure-btn" on:click={measure} disabled={isMeasuring}>
    {isMeasuring ? 'Measuring...' : 'Measure Collapse'}
  </button>
</div>

<style>
  .quantum-container {
    background: rgba(10, 10, 20, 0.85);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 215, 0, 0.18);
    border-radius: 16px;
    padding: 2.5rem;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7);
    margin: 2rem auto;
    max-width: 1100px;
  }

  .quantum-title {
    font-size: 2.8rem;
    font-weight: 900;
    color: #ffd700;
    text-align: center;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
    margin-bottom: 0.5rem;
  }

  .quantum-subtitle {
    text-align: center;
    color: #b8975e;
    font-style: italic;
    margin-bottom: 2rem;
  }

  .circuit-wrapper {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
    position: relative;
  }

  .qubit-lines {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-right: 2rem;
  }

  .qubit-line {
    width: 80px;
    height: 60px;
    background: linear-gradient(90deg, #222, #444);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    color: #aaa;
    border: 1px solid #555;
  }

  .gates {
    display: flex;
    gap: 2rem;
    align-items: center;
  }

  .gate {
    width: 70px;
    height: 70px;
    background: #1a1a2e;
    border: 2px solid #ffd700;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    color: #ffd700;
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
  }

  .measure {
    background: #ffd700;
    color: #000;
  }

  .branches {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
  }

  .branch-card {
    background: rgba(20, 20, 40, 0.7);
    border: 1px solid rgba(255, 215, 0, 0.15);
    border-radius: 12px;
    overflow: hidden;
    cursor: pointer;
    transition: all 0.4s ease;
  }

  .branch-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
  }

  .branch-header {
    padding: 1rem;
    font-weight: bold;
    text-align: center;
    color: white;
    font-size: 1.1rem;
  }

  .branch-body {
    padding: 1.5rem;
    text-align: center;
  }

  .collapse-result {
    margin-top: 1rem;
    padding: 0.8rem;
    background: rgba(0, 255, 136, 0.2);
    border-radius: 8px;
    color: #00ff88;
    font-weight: bold;
  }

  .probability-bar {
    height: 8px;
    background: #333;
    margin: 1rem 1.5rem;
    border-radius: 4px;
    overflow: hidden;
  }

  .bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #ffd700, #ffaa00);
    transition: width 1.2s ease-out;
  }

  .measure-btn {
    display: block;
    margin: 2rem auto;
    padding: 1rem 2.5rem;
    background: #ffd700;
    color: #000;
    font-size: 1.3rem;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.3s;
  }

  .measure-btn:hover:not(:disabled) {
    transform: scale(1.05);
    box-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
  }

  .measure-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
</style>
