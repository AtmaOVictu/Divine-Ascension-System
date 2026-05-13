import { useEffect, useState } from "react";

import { Panel } from "../components/Panel";
import { simulationPath, type SimulationCase, type TruthUnit } from "../domain/types";

type SimulationLabViewProps = {
  simulations: SimulationCase[];
  truthUnits: TruthUnit[];
};

export function SimulationLabView(props: SimulationLabViewProps): JSX.Element {
  const [activeIndex, setActiveIndex] = useState(0);
  const simulation = props.simulations[0] ?? null;

  useEffect(() => {
    const timer = window.setInterval(() => {
      setActiveIndex((current) => (current + 1) % simulationPath.length);
    }, 1700);

    return () => {
      window.clearInterval(timer);
    };
  }, []);

  if (!simulation) {
    return (
      <div className="view-grid">
        <Panel title="Simulation Lab">
          <div className="stack">
            <p className="muted">Simulacijski primer še ni pripravljen.</p>
            <p className="muted">Dodaj ali uvozi stanje, ki vsebuje simulacijski primer.</p>
          </div>
        </Panel>
      </div>
    );
  }

  return (
    <div className="view-grid">
      <Panel title="Simulation Lab">
        <div className="stack">
          <div>
            <strong>{simulation.title}</strong>
            <p className="muted">{simulation.description}</p>
          </div>
          <div className="stepper">
            {simulation.steps.map((step, index) => {
              const className =
                index === activeIndex ? "step active" : index < activeIndex ? "step done" : "step";
              return (
                <article key={step.status} className={className}>
                  <div className="step-index">{index + 1}</div>
                  <strong>{step.status}</strong>
                  <p className="muted">{step.note}</p>
                </article>
              );
            })}
          </div>
          <div className="panel" style={{ padding: "1rem" }}>
            <strong>Aktivni korak</strong>
            <p className="muted">{simulation.steps[activeIndex]?.note}</p>
            <div className="badge-row">
              {props.truthUnits
                .filter((unit) => simulation.involvedUnitIds.includes(unit.id))
                .map((unit) => (
                  <span key={unit.id} className="badge accent">
                    {unit.title}
                  </span>
                ))}
            </div>
          </div>
        </div>
      </Panel>
    </div>
  );
}
