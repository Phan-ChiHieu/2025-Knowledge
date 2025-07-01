'use cache';

import db from '#/lib/db';
import { Boundary } from '#/ui/boundary';
import { type Metadata } from 'next';
import readme from './readme.mdx';
import { Mdx } from '#/ui/codehike';
import { Tabs } from '#/ui/tabs';
import { ClickCounter } from '#/ui/click-counter';

export async function generateMetadata(): Promise<Metadata> {
  const demo = db.demo.find({ where: { slug: 'layouts' } });

  return {
    title: demo.name,
    openGraph: { title: demo.name, images: [`/api/og?title=${demo.name}`] },
  };
}

export default async function Layout({
  children,
}: {
  children: React.ReactNode;
}) {
  const demo = db.demo.find({ where: { slug: 'layouts' } });
  const sections = db.section.findMany();

  return (
    <>
      <Boundary label="Demo" kind="solid" animateRerendering={false}>
        <Mdx source={readme} collapsed={true} />
      </Boundary>
      <Boundary
        label="layout.tsx"
        kind="solid"
        animateRerendering={false}
        className="flex flex-col gap-9"
      >
        <div className="flex justify-between">
          <Tabs
            basePath={`/${demo.slug}`}
            items={[
              { text: 'Home' },
              ...sections.map((x) => ({ text: x.name, slug: x.slug })),
            ]}
          />

          <div className="self-start">
            <ClickCounter />
          </div>
        </div>

        {children}
      </Boundary>
    </>
  );
}
