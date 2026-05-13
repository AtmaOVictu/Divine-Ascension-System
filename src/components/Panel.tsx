import type { ReactNode } from "react";

type PanelProps = {
  title: string;
  children: ReactNode;
  rightSlot?: ReactNode;
};

export function Panel({ title, children, rightSlot }: PanelProps): JSX.Element {
  return (
    <section className="panel">
      <div className="row">
        <h3>{title}</h3>
        {rightSlot}
      </div>
      {children}
    </section>
  );
}
