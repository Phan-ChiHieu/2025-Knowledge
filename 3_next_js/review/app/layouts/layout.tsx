'use cache';

import db from '#/lib/db';
import { Boundary } from '#/ui/boundary';
import { type Metadata } from 'next';
import readme from './readme.mdx';
import { Mdx } from '#/ui/codehike';

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
      {children}
    </>
  );
}
