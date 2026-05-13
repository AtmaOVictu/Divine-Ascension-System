import { Panel } from "../components/Panel";
import { relationTypeLabels, type TruthUnit, type UnitLink } from "../domain/types";

type OntographViewProps = {
  truthUnits: TruthUnit[];
  links: UnitLink[];
};

export function OntographView(props: OntographViewProps): JSX.Element {
  return (
    <div className="view-grid">
      <Panel title="Ontograph relacije">
        {props.links.length === 0 ? (
          <div className="callout">
            <strong>Ni še relacij.</strong>
            <p className="muted">Relacije nastanejo šele, ko obstajajo enote in povezave med njimi.</p>
          </div>
        ) : (
          <div className="link-list">
            {props.links.map((link) => {
              const fromTitle = props.truthUnits.find((unit) => unit.id === link.fromUnitId)?.title ?? "Vir";
              const toTitle = props.truthUnits.find((unit) => unit.id === link.toUnitId)?.title ?? "Cilj";

              return (
                <article key={link.id} className="link-item">
                  <strong>
                    {fromTitle}
                    {" -> "}
                    {link.relationType}
                    {" -> "}
                    {toTitle}
                  </strong>
                  <p className="muted">{relationTypeLabels[link.relationType]}: {link.note}</p>
                </article>
              );
            })}
          </div>
        )}
      </Panel>
    </div>
  );
}
