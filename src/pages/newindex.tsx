import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";

type SingleCardProps = {
  test: string;
};

const Home: NextPage = () => {
  return (
    <>
      <Head>
        <title>Just TCG Analytics</title>
        <meta
          name="description"
          content="Analytics and price guides for the justtcg website"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="container mx-auto flex flex-col items-center justify-center min-h-screen p-4">
        <div className="grid gap-3 pt-3 mt-3 md:grid-cols-4 lg:w-80%">
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
          <SingleCard test="test" />
        </div>
      </main>
    </>
  );
};

const SingleCard = ({ test }: SingleCardProps) => {
  return (
    <section className="flex flex-col p-2 border-2 border-gray-400 rounded flex-start shadow-lg text-left min-w-fit motion-safe:hover:scale-105 duration-500">
      <Image
        className="object-contain mt-0 shadow-lg"
        src="https://static.cardmarket.com/img/bb859795208585689e5a773fef8df5b8/items/1/2X2/665736.jpg"
        alt="Picture of the card"
        width={200}
        height={100}
      />
      <h1 className="text-2xl text-gray-900">Card Name</h1>
      <h2 className="text-xl text-gray-900">Card Expansion</h2>
      <h2 className="text-xl underline underline-offset-2 text-gray-900">
        Prices
      </h2>
      <div className="flex">
        <div className="flex flex-col">
          <p className="text-lg text-gray-700">Cardmarket Low:</p>
          <p className="text-lg text-gray-700">Cardmarket Low CH:</p>
          <p className="text-lg text-gray-700">Cardmarket Trend:</p>
          <p className="text-lg text-gray-700">Magic Monk:</p>
          <p className="text-lg text-gray-700">The Mana Shop:</p>
          <p className="text-lg text-gray-700">Just TCG:</p>
        </div>
        <div className="ml-5">
          <p className="text-lg text-gray-500">10CHF</p>
          <p className="text-lg text-gray-500">11</p>
          <p className="text-lg text-gray-500">12</p>
          <p className="text-lg text-gray-500">13</p>
          <p className="text-lg text-gray-500">14</p>
          <p className="text-lg text-gray-500">15</p>
        </div>
      </div>
    </section>
  );
};

export default Home;
