import { startTransition } from "react";

import { viewLabels, type ViewId } from "../domain/types";

type NavigationProps = {
  view: ViewId;
  truthUnitsCount: number;
  documentsCount: number;
  onViewChange: (next: ViewId) => void;
};

export function Navigation(props: NavigationProps): JSX.Element {
  return (
    <aside className="sidebar">
      <div className="brand">
        <p className="muted">JEWIK</p>
        <h1 className="brand-name">Truthbase Studio</h1>
        <p className="brand-copy">
          Lokalni delovni studio za dokumente, kandidate za resnico, definicije, dokazno pot in
          osebni kanon.
        </p>
      </div>

      <div className="panel" style={{ marginBottom: "1rem" }}>
        <div className="stack">
          <div className="row">
            <span className="muted">Dokumenti</span>
            <strong>{props.documentsCount}</strong>
          </div>
          <div className="row">
            <span className="muted">Truth units</span>
            <strong>{props.truthUnitsCount}</strong>
          </div>
        </div>
      </div>

      <div className="nav-list">
        {viewLabels.map((item) => (
          <button
            key={item.id}
            className={`nav-item ${props.view === item.id ? "active" : ""}`}
            onClick={() => {
              startTransition(() => {
                props.onViewChange(item.id);
              });
            }}
          >
            <strong>{item.label}</strong>
            <span className="muted">{item.hint}</span>
          </button>
        ))}
      </div>
    </aside>
  );
}
